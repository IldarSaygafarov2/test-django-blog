var swiper = new Swiper(".mySwiper", {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});


const url = 'https://djangoblogvtpt1930.pythonanywhere.com/api/v1'

fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data)
  })