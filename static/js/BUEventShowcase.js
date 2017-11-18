var BUEventShowcase={
}
BUEventShowcase.documentReady=function(){
	console.log("BUEventShowcase is ready");
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