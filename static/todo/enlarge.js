control = false;
buttonclick=false;
clicked = false;

function enlarge(item_pk){
	clicked_item = item_pk;
	clicked = true
}

function checkclick(){
	if ((control == false)&&(clicked)&&(buttonclick==false)){
		control = true;
		clicked = false;
		item = document.getElementById('todo'+clicked_item);
		fulltitle = item.getElementsByClassName('fulltitle')[0].textContent;
		shorttitle = item.getElementsByClassName('todotitle')[0].textContent;
		fulldisc = item.getElementsByClassName('fulldisc')[0].textContent;
		shortdisc = item.getElementsByClassName('tododisc')[0].textContent;
		item.getElementsByClassName('todotitle')[0].textContent = fulltitle;
		item.getElementsByClassName('tododisc')[0].textContent = fulldisc;
		item.classList.value += ' enlarge';
		
	};
	buttonclick=false
	clicked=false
};

window.addEventListener('keydown' , (event) => {
	if (event.key == "Escape"){
		if (control){
			item.getElementsByClassName('todotitle')[0].textContent = shorttitle;
			item.getElementsByClassName('tododisc')[0].textContent = shortdisc;
			control = false;
			item.classList.value = item.classList.value.split(' ').slice(0,2).join(' ');
		};
		addform.id = 'hidden';
		editform.id = 'hidden';
	};
});

window.addEventListener('click' , (event) => {
		if (String(event.path[0])=="[object HTMLButtonElement]"){
			buttonclick=true;
		}
	}
);

window.setInterval(checkclick , 100);
