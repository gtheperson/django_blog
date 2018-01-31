// javascript for blog

// for the archive make clicking on the month reveal the posts in that month

var monthDiv = document.getElementsByClassName('month-div');
// this is a list so we need to loop through it to add eventlisteners to each item
for (i = 0; i < monthDiv.length; i++) {
	// the bind allows us to pass the index to the function without calling the function
	monthDiv[i].addEventListener("click", expandMonth.bind(null, i));
}
// if the month has been clicked minimise the posts, otherwise expand them
function expandMonth(index) {
	if (monthDiv[index].getElementsByClassName("monthly-post-div")[0].classList.contains("clicked-monthly")) {
		monthDiv[index].getElementsByClassName("monthly-post-div")[0].classList.remove("clicked-monthly");
	} else {
	monthDiv[index].getElementsByClassName("monthly-post-div")[0].classList.add("clicked-monthly");
	}
}

