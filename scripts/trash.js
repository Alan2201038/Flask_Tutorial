// MQTT Broker URL
const central_hub = "192.168.10.191:1883"

// Create an MQTT client instance
const options = {
  // Clean session
  clean: true,
  connectTimeout: 4000,
  // Authentication
  username: 'admin',
  password: 'password',
}

// Create an MQTT client
var client = mqtt.connect("192.168.10.191:1883");

// MQTT on connect event handler
client.on("connect", function() {
  console.log("Connected to MQTT broker");

  // Subscribe to the trash topic
  client.subscribe("/trash");
});

// MQTT on message event handler
client.on("message", function(topic, message) {
  if (topic === "/trash") {
    var trashLevel = parseFloat(message.toString()); // Convert the message to a float number
    document.getElementById("trash-level").textContent = trashLevel.toFixed(2) + "%"; // Update the trash level in the HTML
  }
});
