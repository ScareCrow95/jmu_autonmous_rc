const carHandler = require('./components/car')
const remoteHandler = require('./components/remote')
let remoteNsp = {}
let carNsp = {}

module.exports = io => {
  remoteNsp = io.of('/remote')
  carNsp = io.of('/car')
  remoteHandler(remoteNsp, io)
  carHandler(carNsp, io)
}
