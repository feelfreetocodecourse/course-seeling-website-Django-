var player;
var video_list
document.onreadystatechange = function () {
    if (document.readyState == 'interactive') {
        player = document.getElementById("player")
        video_list = document.getElementById("video_list")
        
        maintainRatio()
    }
}
function maintainRatio() {
    var w = player.clientWidth
    var h = (w * 9) / 16
    console.log({ w, h });
    player.height = h
    video_list.style.maxHeight = h + "px"
}
window.onresize = maintainRatio