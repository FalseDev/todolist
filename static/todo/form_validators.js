editform = document.getElementsByName('editform')[0];
addform = document.getElementsByName('addform')[0];

function showedit(q_id_inp){
	editform.id = 'visible';
	q_id = q_id_inp
}

function add(){
	addform.id = 'visible';
}

function edit(){
	nameField = document.getElementById('nameedit');
	textField = document.getElementById('textedit');
	colorField = document.getElementById('coloredit');
	priorField = document.getElementById('priorityedit');

	if ((nameField.value == '') | (textField.value == '')){
		alert("Empty Field!")
	}
	else {
		window.location = ('/edit/' + q_id + '/' + nameField.value + '/' + textField.value + '/' + colorField.value + '/' + priorField.value + '/');
	}
};

function submit(){
	nameField = document.getElementById('name');
	textField = document.getElementById('text');
	colorField = document.getElementById('color');
	priorField = document.getElementById('priority');
	if ((nameField.value == '') | (textField.value == '')){
		alert("Empty Field!")
	}
	else {
	window.location = ('/add/' + nameField.value + '/' + textField.value + '/' + colorField.value + '/' + priorField.value + '/');
	}
}
