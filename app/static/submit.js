$( document ).ready(function() {
	$('#brand').select2({
    minimumInputLength: 3
});
	$('#clothing_type').select2();
	$('#colour').select2();
	$('#country').select2();
	$('#store').select2();
	$('#currency').select2();
	console.log( "ready!" );
});
