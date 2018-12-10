// $(document).ready(function(){

// 	$('#search-name').keyup(function(){

// 		$.ajax({

// 			type:"POST",
// 			url:"/search_users/",
// 			data:{
// 				'search_text': $('#search-name').val(),
// 				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
// 			},
// 			success: searchSuccess,
// 			dataType: 'html'
// 		});
// 	});
// });

// function searchSuccess(data, textSuccess, jqXHR)
// {
// 	$('#search-results').html(data);
// }


$(document).ready(function(){

	$('#search-name').keyup(function(){

		$.ajax({

			type:"POST",
			url:"/search_users/",
			data:{
				'search_text': $('#search-name').val(),
