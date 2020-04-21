module.exports = (nsp, io) => {
  nsp.on('connection', (socket) => {
    console.log('remote connected')

    socket.emit('remote connected')

    socket.emit('success')

    socket.on('throttle', (data) => {
      console.log(data)
      eventManager.emit('throttle', data)
    })

    socket.on('record', (data) => {
      console.log(data)
      eventManager.emit('record')
    })

    socket.on('stopRecording', (data) => {
      console.log(data)
      eventManager.emit('stopRecording')
    })

    socket.on('changeSpeed', (data) => {
      console.log(data)
      eventManager.emit('changeSpeed', data)
    })

    socket.on('idle', (data) => {
      eventManager.emit('idle')
    })

    socket.on('stop', (data) => {
      eventManager.emit('stop')
    })

    socket.on('steer', (data) => {
      try {
        console.log(data)
        const jsonData = JSON.parse(data)
        eventManager.emit('steer', jsonData)
      } catch (error) {}
    })
  })
}
