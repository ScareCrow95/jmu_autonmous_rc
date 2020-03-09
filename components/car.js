module.exports = (nsp, io) => {
  eventManager.on('throttle', data => {
    nsp.emit('throttle', data)
  })

  eventManager.on('steer', data => {
    nsp.emit('steer', data)
  })

  eventManager.on('changeSpeed', data => {
    nsp.emit('changeSpeed', data)
  })

  eventManager.on('idle', () => {
    nsp.emit('idle')
  })

  eventManager.on('stop', () => {
    nsp.emit('stop')
  })

  nsp.on('connection', socket => {
    console.log('cart connected')
    console.log('cart connected')
    console.log('cart connected')
    socket.emit('success')

    socket.on('video', data => {
      console.log(data)
    })

    socket.on('k', data => {
      console.log(data)
    })
  })
}
