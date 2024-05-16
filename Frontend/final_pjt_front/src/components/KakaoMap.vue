<template>
  <div>
    <h1 class="ercword">지역별 은행</h1>
    <!-- 검색 입력 부분을 상단으로 이동 -->
    <div class="search-container">
      <select id="keyword" class="custom-border">
        <option value="">은행 선택</option>
        <option value="국민은행">국민은행</option>
        <option value="기업은행">기업은행</option>
        <option value="농협은행">농협은행</option>
        <option value="새마을금고">새마을금고</option>
        <option value="신한은행">신한은행</option>
        <option value="우리은행">우리은행</option>
        <option value="하나은행">하나은행</option>
      </select>
      <input type="text" id="region" size="15" placeholder="지역 입력" class="custom-border" />
      <button @click="searchPlaces" class="custom-border">조회</button>
    </div>
    <!-- 지도 및 결과 영역 -->
    <div class="container custom-border">
      <div id="map" class="map"></div>
      <div id="menu_wrap" class="bg_white">
        <ul id="placesList"></ul>
        <div id="pagination"></div>
      </div>
    </div>
  </div>
</template>

<script>
import mapMarkerImage from '@/assets/mapmarker.png';

export default {
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      this.addKakaoMapScript();
    }
  },
  methods: {
    addKakaoMapScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${import.meta.env.VITE_KAKAO_API_KEY}&libraries=services`;
      document.head.appendChild(script);
    },
    initMap() {
      navigator.geolocation.getCurrentPosition(position => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        const mapContainer = document.getElementById("map");
        const mapOption = {
          center: new kakao.maps.LatLng(36.354946759143, 127.29980994578),
          level: 3,
        };

        this.map = new kakao.maps.Map(mapContainer, mapOption);
        this.ps = new kakao.maps.services.Places();
        this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
        this.markers = [];
      });
    },
    searchPlaces() {
      const keyword = document.getElementById("keyword").value.trim();
      const region = document.getElementById("region").value.trim();

      if (!keyword || !region) {
        alert("키워드와 지역을 모두 입력해주세요!");
        return;
      }

      const query = keyword + ' ' + region;

      this.ps.keywordSearch(query, this.placesSearchCB.bind(this));
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById("placesList");
      const bounds = new kakao.maps.LatLngBounds();

      this.removeAllChildNodes(listEl);
      this.removeMarker();

      places.forEach((place, i) => {
        const placePosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i);
        const itemEl = this.getListItem(i, place);

        bounds.extend(placePosition);

        kakao.maps.event.addListener(marker, "mouseover", () => {
          this.displayInfowindow(marker, place.place_name);
        });

        kakao.maps.event.addListener(marker, "mouseout", () => {
          this.infowindow.close();
        });

        itemEl.onmouseover = () => {
          this.displayInfowindow(marker, place.place_name);
        };

        itemEl.onmouseout = () => {
          this.infowindow.close();
        };

        listEl.appendChild(itemEl);
      });

      this.map.setBounds(bounds);
    },
    getListItem(index, place) {
      const el = document.createElement("li");
      const itemStr = `
        <span class="markerbg marker_${index + 1}"></span>
        <div class="info">
          <h5>${place.place_name}</h5>
          ${place.road_address_name ? `<span>${place.road_address_name}</span><span class="jibun gray">${place.address_name}</span>` : `<span>${place.address_name}</span>`}
          <span class="tel">${place.phone}</span>
        </div>
      `;
      el.innerHTML = itemStr;
      el.className = "item";
      return el;
    },
    addMarker(position, idx) {
      const imageSrc = mapMarkerImage;
      const imageSize = new kakao.maps.Size(36, 37);
      const imgOptions = {
        offset: new kakao.maps.Point(18, 37),
      };
      const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
      const marker = new kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      return marker;
    },
    removeMarker() {
      this.markers.forEach((marker) => marker.setMap(null));
      this.markers = [];
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");

      this.removeAllChildNodes(paginationEl);

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;
        el.className = pagination.current === i ? "on" : "";
        el.onclick = () => {
          pagination.gotoPage(i);
        };
        paginationEl.appendChild(el);
      }
    },
    displayInfowindow(marker, title) {
      const content = `<div style="padding:5px;z-index:1;">${title}</div>`;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    removeAllChildNodes(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
  },
};
</script>

<style>
.container {
  display: flex;
  max-width: 1500px;
  margin: 0 auto;
}
.map {
  width: 70%; /* 지도 영역을 넓게 */
  height: 600px; /* 높이 조정 */
}
.bg_white {
  width: 30%;
  background: #007bff;
  color: black;
  overflow-y: auto;
  height: 600px; /* 높이 조정 */
}
.option {
  padding: 10px 10px 0;
}
#placesList .item {
  padding: 10px;
  border-bottom: 1px solid #e2e2e2;
}
#pagination a {
  margin: 0 2px;
  padding: 3px 6px;
  border: 1px solid #e2e2e2;
  color: #333;
  text-decoration: none;
  cursor: pointer;
}
#pagination a.on {
  border-color: #007bff;
  color: #007bff;
}

.ercword {
  color: #000;
}

.custom-border {
  border: 2px solid #007bff;
  margin: 2px;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}
</style>
