var BUEventShowcase={
	logger : null
}

BUEventShowcase.documentReady =function() {
	console.log("BUEventShowcase is ready");
	BUEventShowcase.buildEventsTable(items);
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
};
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



var items = [
{ eventName: "Event", organizer: "Chirag", participants : "100000", description : "socks only", registrationRequired : "NO", location : "Boston, MA", address : "IDK", city : "Boston", startTime : "69:00", endTime : "96:00", duration : "69hrs", _id : "69", cost : "69", minCost : "69", maxCost : "69", refundPolicy : "NONE", subOrganizers : "69", sponsors : "69"},
{ eventName: "NA", organizer: "80", participants : "3", description : "240", registrationRequired : "3", location : "3", address : "3", city : "3", startTime : "3", endTime : "3", duration : "3", _id : "3", cost : "3", minCost : "3", maxCost : "3", refundPolicy : "3", subOrganizers : "3", sponsors : "3"},
{ eventName: "Apple", organizer: "80", participants : "3", description : "240", registrationRequired : "3", location : "3", address : "3", city : "3", startTime : "3", endTime : "3", duration : "3", _id : "3", cost : "3", minCost : "3", maxCost : "3", refundPolicy : "3", subOrganizers : "3", sponsors : "3"},
{ eventName: "Apple", organizer: "80", participants : "3", description : "240", registrationRequired : "3", location : "3", address : "3", city : "3", startTime : "3", endTime : "3", duration : "3", _id : "3", cost : "3", minCost : "3", maxCost : "3", refundPolicy : "3", subOrganizers : "3", sponsors : "3"},
             ];
BUEventShowcase.buildEventsTable = function(items) {
	console.log(items);
	// clear table contents and set up spotify headers
	resultsTable = $("#resultsTable1");
	$("#resultsTable1" + " tr:has(td)").remove();
	resultsTable.find("thead").remove();
	var header = "<thead><tr><th>eventName</th><th>organizer</th><th>participants</th><th>description</th><th>registrationRequired</th><th>location</th><th>address</th><th>city</th><th>startTime</th><th>endTime</th><th>duration</th><th>_id</th><th>cost</th><th>minCost</th><th>maxCost</th><th>refundPolicy</th><th>subOrganizers</th><th>sponsors</th></tr></thead>";
	resultsTable.prepend(header);
	resultsTableBody = resultsTable.find("tbody");
	for (var i = 0; i < items.length; i++) {
		resultsTableBody.append($('<tr/>').append($('<td/>').append($("<span/>").text(items[i].eventName))).append($('<td/>').append($("<a/>").text(items[i].organizer))).append($('<td/>').append($("<a/>").text(items[i].participants))).append($('<td/>').append($("<a/>").text(items[i].description))).append($('<td/>').append($("<a/>").text(items[i].registrationRequired))).append($('<td/>').append($("<a/>").text(items[i].location))).append($('<td/>').append($("<a/>").text(items[i].address))).append($('<td/>').append($("<a/>").text(items[i].city))).append($('<td/>').append($("<a/>").text(items[i].startTime))).append($('<td/>').append($("<a/>").text(items[i].endTime))).append($('<td/>').append($("<a/>").text(items[i].duration))).append($('<td/>').append($("<a/>").text(items[i]._id))).append($('<td/>').append($("<a/>").text(items[i].cost))).append($('<td/>').append($("<a/>").text(items[i].minCost))).append($('<td/>').append($("<a/>").text(items[i].maxCost))).append($('<td/>').append($("<a/>").text(items[i].refundPolicy))).append($('<td/>').append($("<a/>").text(items[i].subOrganizers))).append($('<td/>').append(items[i].sponsors)));
	}
};