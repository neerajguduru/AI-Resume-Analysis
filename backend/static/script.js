let currentResumeText = "";
    let currentJobDescription = "";

    function showUploading() {
      const uploadStatus = document.getElementById("uploadStatus");
      const file = document.getElementById("resume").files[0];
      
      if (file) {
        uploadStatus.style.display = "block";
        uploadStatus.className = "status-message uploading";
        uploadStatus.innerHTML = "⬆️ Uploading " + file.name + "...";
        
        setTimeout(() => {
          uploadStatus.className = "status-message success";
          uploadStatus.innerHTML = "✅ " + file.name + " uploaded successfully!";
        }, 1000);
      }
    }

    async function send() {
      const file = document.getElementById("resume").files[0];
      const jd = document.getElementById("jd").value;
      const output = document.getElementById("output");
      const spinner = document.getElementById("spinner");
      const button = document.querySelector(".analyze-btn");
      const resultsSection = document.getElementById("resultsSection");
      const qaSection = document.getElementById("qaSection");

      if (!file || !jd.trim()) {
        alert("Please upload a resume and paste job description.");
        return;
      }

      button.disabled = true;
      button.textContent = "🔍 Analyzing...";
      spinner.style.display = "block";
      output.innerHTML = "";
      resultsSection.style.display = "none";

      const form = new FormData();
      form.append("resume", file);
      form.append("job_description", jd);

      try {
        const res = await fetch("/api/analyze_with_gemini", {
          method: "POST",
          body: form
        });

        const data = await res.json();
        
        currentResumeText = data.resume_text || "";
        currentJobDescription = jd;
        
        let analysis = data.gemini_analysis || "❌ Failed to get response.";
        analysis = analysis
          .replace(/^([A-Z][^\n:]+):/gm, "<strong>$1:</strong>")
          .replace(/^\* (.+)$/gm, "<li>$1</li>");
        if (analysis.includes("<li>")) {
          analysis = analysis.replace(/(<li>[\s\S]+?<\/li>)/g, "<ul>$1</ul>");
        }
        
        output.innerHTML = analysis;
        resultsSection.style.display = "block";
        qaSection.style.display = "block";
        
        // Smooth scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
        
      } catch (error) {
        output.innerHTML = "❌ Error occurred while analyzing the resume.";
        resultsSection.style.display = "block";
      } finally {
        spinner.style.display = "none";
        button.disabled = false;
        button.textContent = "✨ Analyze with AI";
      }
    }

    async function askQuestion() {
      const questionInput = document.getElementById("questionInput");
      const question = questionInput.value.trim();
      const qaOutput = document.getElementById("qa-output");
      const qaSpinner = document.getElementById("qaSpinner");
      const askButton = document.querySelector(".ask-btn");

      if (!question) {
        alert("Please enter a question.");
        return;
      }

      if (!currentResumeText) {
        alert("Please analyze your resume first before asking questions.");
        return;
      }

      askButton.disabled = true;
      askButton.textContent = "🤔 Asking...";
      qaSpinner.style.display = "block";
      qaOutput.style.display = "none";

      try {
        const res = await fetch("/api/ask_question", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            question: question,
            resume_text: currentResumeText,
            job_description: currentJobDescription
          })
        });

        const data = await res.json();
        
        qaOutput.innerHTML = data.answer || "❌ Failed to get response.";
        qaOutput.style.display = "block";
        questionInput.value = "";
        
      } catch (error) {
        qaOutput.innerHTML = "❌ Error occurred while processing your question.";
        qaOutput.style.display = "block";
      } finally {
        qaSpinner.style.display = "none";
        askButton.disabled = false;
        askButton.textContent = "🤔 Ask AI";
      }
    }

    // Enter key to submit question
    document.getElementById("questionInput").addEventListener("keypress", function(e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        askQuestion();
      }
    });