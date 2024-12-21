const speakButton = document.getElementById("speakButton");
const summaryText = document.getElementById("summaryText");
const audioPlayer = document.createElement("audio");

speakButton.addEventListener("click", async () => {
  const text = summaryText.innerText;

  if (!text.trim()) {
    alert("No text!");
    return;
  }
  const userConfirmation = confirm("Do you really wish to play the audio?");
  
  if (!userConfirmation) {
    alert("Audio playback cancelled.");
    return;
  }
  try {
    const response = await fetch("/speak", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    if (!response.ok) {
      throw new Error(`${response.status}`);
    }
    const result = await response.json();
    if (result.status === "success") {
      audioPlayer.src = result.audio;
      audioPlayer.play();
    } else {
      alert(`${result.message}`);
    }
  } catch (error) {
    alert(`${error.message}`);
  }
});

const copyButton = document.getElementById("copyButton");

copyButton.addEventListener("click", function () {
  const textToCopy = document.getElementById("summaryText").innerText;
  navigator.clipboard.writeText(textToCopy)
  .then(() => {
    alert("Text copied to clipboard!");
  })
  .catch(err => {
    alert("Failed to copy the text: " + err);
  });
});




// const speakButton = document.getElementById("speakButton");
// const summaryText = document.getElementById("summaryText");

// speakButton.addEventListener("click", () => {
//   const text = summaryText.innerText;

//   fetch("/speak", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ text }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.error) {
//         alert(data.error);
//       } else {
//         alert(data.message);
//       }
//     })
//     .catch((error) => console.error("Error:", error));
// });
