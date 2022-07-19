
// const handler = () => {
//     alert("hello");
// }

const save_tabs = () => {
    // const tabs = []
    chrome.tabs.query({}, function(tabs) {
        tabs.forEach(function (tab) {
            // console.log(tab);
            console.log(tab.windowId, tab.url, tab.title, tab.favIconUrl);
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("save_tabs_button").addEventListener("click", save_tabs);
});
