
window.onload = function () {
	const colour_btn_els = document.querySelectorAll('.colours .colour');
	const sizes_btn_els = document.querySelectorAll('.sizes .size');
	const imagery_el = document.querySelector('.imagery');
	const image_el = document.querySelector('.imagery .image');

	for (let i = 0; i < sizes_btn_els.length; i++) {
		let btn = sizes_btn_els[i];

		btn.addEventListener('click', function () {
			document.querySelector('.sizes .size.selected').classList.remove('selected');
			this.classList.add('selected');
		});
	}

	for (let i = 0; i < colour_btn_els.length; i++) {
		let btn = colour_btn_els[i];

		btn.addEventListener('click', function () {
			document.querySelector('.colours .colour.selected').classList.remove('selected');
			this.classList.add('selected');
			image_el.src = "{% static 'main/img/tsh-' %}" + this.dataset.name + '.png';
		});
	}