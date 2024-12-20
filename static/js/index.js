const navbarItem = document.getElementById("toggleNavbarItem");
const iframe = document.getElementById("myIframe");
const myh3 = document.getElementById("myh3");

navbarItem.addEventListener("click", (event) => {
  event.preventDefault();
  if (iframe.style.display === "none" || iframe.style.display === "") {
    iframe.style.display = "block";
    myh3.style.display = "none";
    navbarItem.textContent = "Hide Content";
  } else {
    iframe.style.display = "none";
    myh3.style.display = "block";
    navbarItem.textContent = "How to use";
  }
});
