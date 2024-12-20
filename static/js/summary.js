const speakButton = document.getElementById("speakButton");
      const summaryText = document.getElementById("summaryText");

      speakButton.addEventListener("click", () => {
        const text = summaryText.innerText;

        fetch("/speak", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text }),
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.error) {
              alert(data.error);
            } else {
              alert(data.message);
            }
          })
          .catch((error) => console.error("Error:", error));
      });