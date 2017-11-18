var BUEventShowcase={
}
BUEventShowcase.documentReady=function(){
	console.log("BUEventShowcase is ready");
}
BUEventShowcase.searchByID = function(){
	ids=$('#idField').val()
	console.log("sending id: ",ids)
	$.post("/searchID",{
		id: ids
	})
	.done(function(response){
		response=JSON.parse(response)
		console.log(response)
	})
}