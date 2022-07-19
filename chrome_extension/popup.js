
// const handler = () => {
//     alert("hello");
// }



const save_tabs = () => {
    chrome.tabs.query({}, function (tabs) {
        const tabs_out = []
        tabs.forEach(function (tab) {
            // console.log(tab)
            // console.log(tab.windowId, tab.url, tab.title, tab.favIconUrl)
            // console.log({url: tab.url, title: tab.title, favIconUrl: tab.favIconUrl, windowId: tab.windowId})
            tabs_out.push({url: tab.url, title: tab.title, favIconUrl: tab.favIconUrl, windowId: tab.windowId})
        })
        const opts = {
            method: 'POST',
            headers: {'content-type': 'application/json'},
            body: JSON.stringify(tabs_out)
        }
        const endpoint = 'http://localhost:5006/'
        fetch(endpoint, opts).then(response => response.json()).then(data => {
            console.log(data)
        })
    })
    // .then(tabs_out => {
    // console.log(tabs_out)
    //
    //     fetch(endpoint, opts).then(response => console.log(response.json()))
    // })
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("save_tabs_button").addEventListener("click", save_tabs)
})
