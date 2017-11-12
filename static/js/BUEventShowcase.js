var BUEventShowcase={
}
BUEventShowcase.searchByID = function(){
	ids=$('#searchIds').val()
	$.post("/searchByID"),{
		ID: ids
	}
	.done(function(response)){
		response=JSON.parse(response)
	}
}