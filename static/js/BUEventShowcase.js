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
BUEventShowcase.create = function(){
	org=$('#org').val()
	location=$('#location').val()
	time=$('#time').val()
	name=$('#name').val()
	console.log("sending id: ",ids)
	$.post("/createEvent",{
		org: org,
		location: location,
		time: time,
		name: name
	})
	.done(function(response){
		response=JSON.parse(response)
		console.log(response)
	})
}