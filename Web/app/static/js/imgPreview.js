function imgPreview(event) {
	if (event.target.files.length > 0) {
		var src = URL.createObjectURL(event.target.files[0]);
		var preview = document.getElementById("photo-preview");
		preview.src = src;
		preview.style.display = "block";
	}
}

function idcardPreview(event) {
	if (event.target.files.length > 0) {
		var src = URL.createObjectURL(event.target.files[0]);
		var preview = document.getElementById("idcard-preview");
		preview.src = src;
		preview.style.display = "block";
	}
}