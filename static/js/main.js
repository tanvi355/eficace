let switch_status = localStorage.getItem("status");

var text = document.getElementById("toggle_font");
var bg = document.getElementById("bdy");
var hname=document.getElementById("hname");
var line=document.getElementsByClassName("hrline");

document.addEventListener("DOMContentLoaded", function() {


	if(switch_status==='dark')
	{
		darkMode();
	}
});


const darkMode=()=>
{
    //add dark mode to the body
        bg.classList.remove("b_light");
		bg.classList.add("b_dark");
		text.innerHTML = "Go Light!";
		text.style.color = "white";
		hname.style.color="whitesmoke";
        line[0].style.backgroundColor="whitesmoke";
        line[1].style.backgroundColor="whitesmoke";

    //change the status in localhost
    localStorage.setItem("status","dark");

}

const lightMode=()=>
{
        bg.classList.remove("b_dark");
		bg.classList.add("b_light");
		text.innerHTML = "Go Dark!";
		text.style.color = "#212121";
		hname.style.color="#212121";
        line[0].style.backgroundColor="#212121";
        line[1].style.backgroundColor="#212121";


        localStorage.setItem("status","light");
}



function change_mode() {

	switch_status = localStorage.getItem("status");


	if (switch_status === 'dark') {
		//change to dark
		lightMode();

	}
    else {
		//change back to light
		darkMode();
	}

}

// to refresh and keep the scroll position
document.addEventListener("DOMContentLoaded", function(event) {
            var scrollpos = localStorage.getItem('scrollpos');
            if (scrollpos) window.scrollTo(0, scrollpos);
        });

        window.onbeforeunload = function(e) {
            localStorage.setItem('scrollpos', window.scrollY);
        };
