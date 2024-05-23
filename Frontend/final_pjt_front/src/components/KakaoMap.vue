<template>
  <div class="container">
    <div class="search-section">
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

        <select id="bigcity" class="custom-border" @change="updateSmallCities">
          <option value="">대분류 지역 선택</option>
          <option v-for="(smallcities, bigcity) in regions" :value="bigcity">{{ bigcity }}</option>
        </select>

        <select id="smallcity" class="custom-border">
          <option value="">소분류 지역 선택</option>
          <option v-for="smallcity in smallCities" :value="smallcity">{{ smallcity }}</option>
        </select>

        <button @click="searchPlaces" class="custom-border">조회</button>
      </div>
    </div>

    <div class="content">
      <div class="map-container custom-border">
        <div id="map" class="map"></div>
      </div>

      <div class="info-container bg_white custom-border">
        <div id="menu_wrap">
          <ol id="placesList"></ol>
          <div id="pagination"></div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import mapMarkerImage from '@/assets/img/mapmarker.png';
import bankLogo_우리은행 from '@/assets/img/우리은행.png';
import bankLogo_하나은행 from '@/assets/img/하나은행.png';
import bankLogo_신한은행 from '@/assets/img/신한은행.png';
import bankLogo_기업은행 from '@/assets/img/기업은행.png';
import bankLogo_새마을금고 from '@/assets/img/새마을금고.png';
import bankLogo_국민은행 from '@/assets/img/국민은행.png';
import bankLogo_농협은행 from '@/assets/img/농협은행.png';

export default {
  data() {
    return {
      showMap: false, // 지도 보이기 여부
      showInfo: false, // 설명 보이기 여부
      regions: {
        강원도: ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군'],
        경기도: ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '부천시 소사구', '부천시 오정구', '부천시 원미구', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시', '안산시 단원구', '안산시 상록구', '안성시', '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'],
        경상남도: ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군', '함안군', '함양군', '합천군'],
        경상북도: ['경산시', '경주시', '고령군', '구미시', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시 남구', '포항시 북구'],
        광주광역시: ['광산구', '남구', '동구', '북구', '서구'],
        대구광역시: ['군위군', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
        대전광역시: ['대덕구', '동구', '서구', '유성구', '중구'],
        부산광역시: ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'],
        서울특별시: ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
        세종특별자치시: ['전체'],
        울산광역시: ['남구', '동구', '북구', '울주군', '중구'],
        인천광역시: ['강화군', '계양구', '남구', '남동구', '동구', '부평구', '서구', '연수구', '옹진군', '중구'],
        전라남도: ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'],
        전북특별자치도: ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시 덕진구', '전주시 완산구', '정읍시', '진안군'],
        제주특별자치도: ['서귀포시', '제주시'],
        충청남도: ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군'],
        충청북도: ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청주시 상당구', '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시'],
      },
      smallCities: []
    };
  },
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
          center: new kakao.maps.LatLng(latitude, longitude), // Update center with current location
          level: 1,
        };

        this.map = new kakao.maps.Map(mapContainer, mapOption);
        this.ps = new kakao.maps.services.Places();
        this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
        this.markers = [];
      });
    },
    updateSmallCities(event) {
      const bigcity = event.target.value;
      this.smallCities = this.regions[bigcity] || [];
    },
    searchPlaces() {
      const bigcity = document.getElementById("bigcity").value.trim(); // 새로운 대분류 지역 변수 추가
      const smallcity = document.getElementById("smallcity").value.trim(); // 소분류 지역 추가
      const keyword = document.getElementById("keyword").value.trim(); // Get selected bank
      const query = `${bigcity} ${smallcity} ${keyword}`; // Concatenate big city, small city, and bank name

      if (!bigcity || !smallcity || !keyword) { // 대분류 지역, 소분류 지역 및 은행을 모두 선택해야 함
        alert("대분류 지역, 소분류 지역 및 은행을 모두 선택해주세요!");
        return;
      }

      this.ps.keywordSearch(query, this.placesSearchCB.bind(this));
      this.showMap = true; // 지도 보이기 설정
    this.showInfo = true; // 설명 보이기 설정
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
      const bankName = document.getElementById("keyword").value.trim(); // 선택된 은행 이름 가져오기

      // 선택된 은행에 따라 적절한 로고 이미지를 선택합니다.
      let logoSrc = '';
      switch(bankName) {
        case '우리은행':
          logoSrc = bankLogo_우리은행;
          break;
        case '하나은행':
          logoSrc = bankLogo_하나은행;
          break;
        case '신한은행':
          logoSrc = bankLogo_신한은행;
          break;
        case '기업은행':
          logoSrc = bankLogo_기업은행;
          break;
        case '새마을금고':
          logoSrc = bankLogo_새마을금고;
          break;
        case '국민은행':
          logoSrc = bankLogo_국민은행;
          break;
        case '농협은행':
          logoSrc = bankLogo_농협은행;
          break;
        // 필요한 만큼 case를 추가합니다.
        default:
          // 선택된 은행 이름에 해당하는 이미지가 없을 경우, 기본 로고 이미지를 사용하거나 처리합니다.
          break;
      }

      const itemStr = `
      <div class="info">
        <img src="${logoSrc}" alt="${bankName}" class="bank-logo" width="15" height="15"> <!-- 은행 로고 이미지 -->
          ${place.place_name}<vbr>
          ${place.road_address_name ? `<span>${place.road_address_name}</span><span class="jibun gray">${place.address_name}</span>` : `<span>${place.address_name}</span>`}
        </div>
        <hr>
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
      this.markers.forEach(marker => marker.setMap(null));
      this.markers = [];
    },
    displayInfowindow(marker, title) {
      const content = `<div style="padding:3px;z-index:1;">${title}</div>`;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    removeAllChildNodes(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");
      this.removeAllChildNodes(paginationEl);

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = "on";
        } else {
          el.onclick = ((i) => {
            return () => {
              pagination.gotoPage(i);
            };
          })(i);
        }

        paginationEl.appendChild(el);
      }
    },
  },
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 90vh;
  padding: 20px;
  box-sizing: border-box;
}

.search-section {
  text-align: center;
  margin-bottom: 20px;
}

.search-container {
  display: flex;
  flex-direction: row;
  margin-bottom: 30px;
  gap: 20px;
  height:50px;
}

select{
  font-size: 20px;
  width: 300px;
  text-align: center;
}

option{
  font-size: 20px;
}

.content {
  display: flex;
  justify-content: center;
  width: 100%;
}

.map-container {
  width: 70%;
  height: 600px;
  margin-bottom: 20px;
}

.info-container {
  width: 20%;
  height: 600px;
  overflow-y: auto;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.custom-border {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.map {
  width: 100%;
  height: 100%;
}

.bg_white {
  background-color: #fff;
}

.ercword {
  margin-bottom: 10px;
}

button.custom-border {
  font-size: 30px;
  width:200px;
  cursor: pointer;
}

#menu_wrap {
  padding: 10px;
}

#placesList .item {
  padding: 10px;
  border-bottom: 1px solid #eee;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#pagination a {
  display: inline-block;
  margin: 0 2px;
  padding: 2px 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
  text-decoration: none;
  color: #333;
}

#pagination a.on {
  background-color: #333;
  color: #fff;
}
</style>
