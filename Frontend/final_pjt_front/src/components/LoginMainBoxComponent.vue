<template>
      <div class="frame-parent1">
        <div class="frame-wrapper1">
          <div class="frame-parent2">
            <div class="frame-wrapper2">
              <div class="parent">
                <h2 class="h2">인기 금융상품</h2>
                <div class="wrapper">
                  <div class="div4">2024. 5. 6 기준</div>
                </div>
              </div>
            </div>
            <div class="frame-parent3">
              <div class="frame">
                <b class="b">한국은행 기준금리</b>
              </div>
              <b class="b1">3.50%</b>
            </div>
          </div>
        </div>
        <div class="backgroundborder-parent">
          <div class="backgroundborder">
            <div class="group">
              <h3 class="h3">정기적금</h3>
              <div class="frame-wrapper3">
                <div class="frame-parent4">
                  <div class="frame-parent5">
                    <div class="wrapper1">
                      <div class="div5">1</div>
                    </div>
                    <img
                      class="image-icon"
                      loading="lazy"
                      alt=""
                      src="/image@2x.png"
                    />
                    <div class="frame-wrapper4">
                      <div class="ibk-parent">
                        <b class="ibk">IBK탄소제로적금(자유적립식)</b>
                        <div class="div6">중소기업은행</div>
                      </div>
                    </div>
                  </div>
                  <div class="frame-parent6">
                    <div class="wrapper2">
                      <div class="div7">2</div>
                    </div>
                    <img class="image-icon1" alt="" src="/image-1@2x.png" />
                    <div class="frame-wrapper5">
                      <div class="mz-parent">
                        <b class="mz">MZ플랜적금</b>
                        <div class="div8">제주은행</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="backgroundborder-inner">
              <div class="frame-parent7">
                <div class="wrapper3">
                  <div class="div9">3</div>
                </div>
                <img class="image-icon2" alt="" src="/image-2@2x.png" />
                <div class="frame-wrapper6">
                  <div class="parent1">
                    <b class="b2">카카오뱅크 26주적금</b>
                    <div class="div10">주식회사 카카오뱅크</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="backgroundborder1">
            <div class="parent2">
              <h3 class="h31">정기예금</h3>
              <div class="frame-wrapper7">
                <div class="frame-parent8">
                  <div class="wrapper4">
                    <div class="div11">1</div>
                  </div>
                  <img class="image-icon3" alt="" src="/image-3@2x.png" />
                  <div class="frame-wrapper8">
                    <div class="the-parent">
                      <b class="the">더(The) 특판 정기예금</b>
                      <div class="div12">부산은행</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="backgroundborder-child">
              <div class="frame-parent9">
                <div class="wrapper5">
                  <div class="div13">2</div>
                </div>
                <img class="image-icon4" alt="" src="/image-4@2x.png" />
                <div class="frame-wrapper9">
                  <div class="parent3">
                    <b class="b3">굿스타트예금</b>
                    <div class="div14">광주은행</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="backgroundborder-inner1">
              <div class="frame-parent10">
                <div class="wrapper6">
                  <div class="div15">3</div>
                </div>
                <img
                  class="dg-logo4b9d3ef2eaf3e404d7dfp-icon"
                  loading="lazy"
                  alt=""
                  src="/dg-logo4b9d3ef2eaf3e404d7dfpng@2x.png"
                />
                <div class="frame-wrapper10">
                  <div class="dgb-parent">
                    <b class="dgb">DGB함께예금</b>
                    <div class="div16">대구은행</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>
<script setup>
  import { defineComponent } from "vue";

</script>
<style scoped>
  .h2 {
    margin: 0;
    flex: 1;
    position: relative;
    font-size: inherit;
    line-height: 28px;
    font-weight: 700;
    font-family: inherit;
    display: inline-block;
    min-width: 116px;
    flex-shrink: 0;
  }
  .div4 {
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 112px;
    flex-shrink: 0;
  }
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-11xs);
    font-size: var(--font-size-base-8);
    color: var(--color-gray-600);
  }
  .parent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-7xs-7);
  }
  .frame-wrapper2 {
    width: 295.7px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    box-sizing: border-box;
  }
  .b {
    align-self: stretch;
    position: relative;
    line-height: 16px;
  }
  .frame {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-8xs);
  }
  .b1 {
    position: relative;
    font-size: var(--font-size-17xl-9);
    line-height: 40px;
    display: inline-block;
    color: var(--color-black);
    min-width: 116px;
    flex-shrink: 0;
  }
  .frame-parent3 {
    width: 251.2px;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-11xs-4);
    font-size: var(--small-text-size);
    color: var(--color-gray-700);
  }
  .frame-parent2 {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    max-width: 100%;
    gap: var(--gap-xl);
  }
  .frame-wrapper1 {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px var(--padding-6xs-8) 0px var(--padding-smi);
    box-sizing: border-box;
    max-width: 100%;
  }
  .h3 {
    margin: 0;
    position: relative;
    font-size: inherit;
    line-height: 22px;
    font-weight: 400;
    font-family: inherit;
    display: inline-block;
    min-width: 88.2px;
  }
  .div5 {
    align-self: stretch;
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 9px;
  }
  .wrapper1 {
    width: 9px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
    box-sizing: border-box;
  }
  .image-icon {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .ibk {
    align-self: stretch;
    position: relative;
    line-height: 18px;
  }
  .div6 {
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: inline-block;
    min-width: 96.2px;
  }
  .ibk-parent {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper4 {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    box-sizing: border-box;
    min-width: 156px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent5 {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-2xs-4);
  }
  .div7 {
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 10px;
  }
  .wrapper2 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
  }
  .image-icon1 {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .mz {
    position: relative;
    line-height: 18px;
    display: inline-block;
    min-width: 100.6px;
  }
  .div8 {
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: inline-block;
    min-width: 64.2px;
  }
  .mz-parent {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper5 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent6 {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs-9);
  }
  .frame-parent4 {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-12xl);
  }
  .frame-wrapper3 {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px var(--padding-9xl-9);
    text-align: center;
    font-size: var(--small-text-size);
  }
  .group {
    width: 347.5px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-base-5);
    max-width: 100%;
  }
  .div9 {
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 11px;
  }
  .wrapper3 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
  }
  .image-icon2 {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .b2 {
    align-self: stretch;
    position: relative;
    line-height: 18px;
    white-space: nowrap;
  }
  .div10 {
    width: 149.8px;
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: flex;
    align-items: center;
  }
  .parent1 {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper6 {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    box-sizing: border-box;
    min-width: 111px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent7 {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs-4);
  }
  .backgroundborder-inner {
    width: 308px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-10xl) 0px var(--padding-9xl-9);
    box-sizing: border-box;
    text-align: center;
    font-size: var(--small-text-size);
  }
  .backgroundborder {
    flex: 1;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-xl);
    background-color: var(--light-text-color);
    border: 1px solid var(--color-gainsboro);
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-20xl) var(--padding-21xl-7) var(--padding-19xl);
    gap: var(--gap-12xl);
    min-width: 382px;
    max-width: 100%;
  }
  .h31 {
    margin: 0;
    position: relative;
    font-size: inherit;
    line-height: 22px;
    font-weight: 400;
    font-family: inherit;
    display: inline-block;
    min-width: 88.2px;
  }
  .div11 {
    align-self: stretch;
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 9px;
  }
  .wrapper4 {
    width: 9px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
    box-sizing: border-box;
  }
  .image-icon3 {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .the {
    align-self: stretch;
    position: relative;
    line-height: 18px;
    white-space: nowrap;
  }
  .div12 {
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: inline-block;
    min-width: 64.2px;
  }
  .the-parent {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper8 {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    box-sizing: border-box;
    min-width: 119px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent8 {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-2xs-4);
  }
  .frame-wrapper7 {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px var(--padding-9xl-9);
    text-align: center;
    font-size: var(--small-text-size);
  }
  .parent2 {
    width: 290.8px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-base-5);
    text-align: left;
    font-size: var(--font-size-3xl);
  }
  .div13 {
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 10px;
  }
  .wrapper5 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
  }
  .image-icon4 {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .b3 {
    position: relative;
    line-height: 18px;
    display: inline-block;
    min-width: 108.2px;
  }
  .div14 {
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: inline-block;
    min-width: 64.2px;
  }
  .parent3 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper9 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent9 {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs-9);
  }
  .backgroundborder-child {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-10xl) 0px var(--padding-9xl-9);
  }
  .div15 {
    position: relative;
    line-height: 16px;
    display: inline-block;
    min-width: 11px;
  }
  .wrapper6 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base-5) 0px 0px;
  }
  .dg-logo4b9d3ef2eaf3e404d7dfp-icon {
    height: 49px;
    width: 49px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .dgb {
    position: relative;
    line-height: 18px;
    display: inline-block;
    min-width: 110.1px;
  }
  .div16 {
    position: relative;
    font-size: var(--small-text-size);
    line-height: 16px;
    display: inline-block;
    min-width: 64.2px;
  }
  .dgb-parent {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-8xs);
  }
  .frame-wrapper10 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-8xs) 0px 0px;
    text-align: left;
    font-size: var(--font-size-lg);
  }
  .frame-parent10 {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs-4);
  }
  .backgroundborder-inner1 {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-10xl) 0px var(--padding-9xl-9);
  }
  .backgroundborder1 {
    flex: 1;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-xl);
    background-color: var(--light-text-color);
    border: 1px solid var(--color-gainsboro);
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-20xl) var(--padding-21xl-7) var(--padding-19xl);
    gap: var(--gap-12xl);
    min-width: 382px;
    max-width: 100%;
    text-align: center;
    font-size: var(--small-text-size);
  }
  .backgroundborder-parent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-18xl);
    max-width: 100%;
    font-size: var(--font-size-3xl);
  }
  .frame-parent1 {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-2xl);
    max-width: 100%;
    font-size: var(--font-size-9xl);
    color: var(--color-black);
    font-family: var(--small-text);
  }


  @media screen and (max-width: 850px) {
    .b1 {
      font-size: var(--font-size-11xl);
      line-height: 32px;
    }

    .frame-parent2 {
      flex-wrap: wrap;
    }

    .backgroundborder {
      min-width: 100%;
    }

    .backgroundborder1 {
      min-width: 100%;
    }

    .backgroundborder-parent {
      gap: var(--gap-lg);
    }

  }
  @media screen and (max-width: 450px) {

    .h2 {
      font-size: var(--font-size-3xl);
      line-height: 22px;
    }

    .parent {
      flex-wrap: wrap;
    }

    .b1 {
      font-size: var(--font-size-3xl);
      line-height: 24px;
    }

    .h3 {
      font-size: var(--font-size-lg);
      line-height: 18px;
    }

    .frame-parent5 {
      flex-wrap: wrap;
    }

    .frame-parent4 {
      gap: var(--gap-mini);
    }

    .frame-parent7 {
      flex-wrap: wrap;
    }

    .backgroundborder {
      gap: var(--gap-mini);
    }

    .h31 {
      font-size: var(--font-size-lg);
      line-height: 18px;
    }

    .frame-parent8 {
      flex-wrap: wrap;
    }

    .frame-parent9 {
      flex-wrap: wrap;
    }

    .frame-parent10 {
      flex-wrap: wrap;
    }

    .backgroundborder1 {
      gap: var(--gap-mini);
    }
  }
</style>
