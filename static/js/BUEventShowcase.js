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
BUEventShowcase.createEvent = function(){
	console.log("Creating event")
	org=$('#org').val()
	Eventlocation=$('#EventLocation').val()
	time=$('#time').val()
	name=$('#name').val()
	console.log("sending Event: ",name)
	$.post("/createEvent",{
		org: org,
		location: Eventlocation,
		time: time,
		name: name
	})
	.done(function(response){
		response=JSON.parse(response)
		console.log(response)
	})
}