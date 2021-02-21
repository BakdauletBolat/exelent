$( () => {
    $(document).ready(function () {
        var hamburger = $("#burger_menu");
        hamburger.click(function () {
        hamburger.toggleClass("active");
        return false;
        });
    });

   
}); 

aboutUs = new Tabber('tabs-item','content_item','tabs');
aboutUs.hideTabContent();
aboutUs.showTabContent(0);
aboutUs.tabView();

tb1 = new Tabber('tb1-item','tc1-item','tb1');
tb1.hideTabContent();
tb1.showTabContent(0);
tb1.tabView();



tb2 = new Tabber('tb2-item','tc2-item','tb2');
tb2.hideTabContent();
tb2.showTabContent(0);
tb2.tabView();

tb3 = new Tabber('tb3-item','tc3-item','tb3');
tb3.hideTabContent();
tb3.showTabContent(0);
tb3.tabView();

tb4 = new Tabber('tb4-item','tc4-item','tb4');
tb4.hideTabContent();
tb4.showTabContent(0);
tb4.tabView();

const btn = document.getElementById('burger_menu');
const menu = document.querySelector('.menu');
btn.addEventListener('click',()=>{
    menu.classList.toggle('active');
})