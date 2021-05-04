// test.js的内容
const video = arguments[0]
const callback = arguments[1]
video.play()
video.playbackRate = 10
video.onended = function(){
    callback('end...');
}
setInterval(function(){
    video.play()
},1000)
