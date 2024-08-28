const socket = new WebSocket('ws://localhost:8765');

function checkElement(element) {
  if (element.tagName === "A" &&
      element.classList.contains("yt-simple-endpoint") &&
      element.getAttribute("href").startsWith("https://www.youtube.com/redirect?event=live_chat") &&
      element.textContent.startsWith("https://pruuu.me")) {
    console.log("Link encontrado:", element.textContent);
    socket.send(element.textContent)
  }
}

const chatContainer = document.getElementById('chat-container');
const iframe = chatContainer.querySelector('iframe')
const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
const container = iframeDocument.getElementById('chat')


const observer = new MutationObserver((mutationsList, observer) => {

  for (let mutation of mutationsList) {
    if (mutation.type === 'childList') {

      mutation.addedNodes.forEach((node) => {

        if (node.nodeType === Node.ELEMENT_NODE) {

          checkElement(node);
        }
      });
    }
  }
});


const config = { childList: true, subtree: true };


observer.observe(container, config);

