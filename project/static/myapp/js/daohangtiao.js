function applySelectedTo(link) {
     var ul = document.getElementsByTagName("ul")[0]; // get the first ul tag on the page
     var allLinks = ul.getElementsByTagName("a"); // get all the links within that ul
     for (var i=0; i<allLinks.length; i++) { // iterate through all those links
      allLinks[i].className = ""; // and assign their class names to nothing
     }
     link.className = "selected"; // finally, assign class="selected" to our chosen link
     var allDivs = document.getElementsByTagName("div");
     for (var k=0; k<allDivs.length; k++) {
      allDivs[k].className = "";
     }
     var lyricId = link.getAttribute("href").split("#")[1];
     lyricId = document.getElementById(lyricId);
     lyricId.className = "on";
    }