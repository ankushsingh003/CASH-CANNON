const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const actionSection = document.getElementById('action-section');

let currentCustomerId = "";

// 1. Chat Logic
function addMessage(text, isUser = false) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    msgDiv.textContent = text;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function handleChat() {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage(text, true);
    userInput.value = "";

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await response.json();

        addMessage(data.response);

        if (data.start_app) {
            highlightActionSection();
        }
    } catch (err) {
        addMessage("Sorry, I'm having trouble connecting right now.");
    }
}

function highlightActionSection() {
    actionSection.style.boxShadow = "0 0 40px rgba(242, 109, 33, 0.4)";
    setTimeout(() => {
        actionSection.style.boxShadow = "0 8px 32px 0 rgba(0, 0, 0, 0.37)";
    }, 2000);
}

sendBtn.addEventListener('click', handleChat);
userInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(); });

// 2. Application Flow Logic
async function verifyCustomer() {
    const cidInput = document.getElementById('customer-id-input');
    const cid = cidInput.value.trim();
    if (!cid) return;

    try {
        const response = await fetch('/api/verify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ customer_id: cid })
        });
        const data = await response.json();

        if (data.status === "VERIFIED") {
            currentCustomerId = cid;
            transitionToStep(2);
        } else {
            alert(data.message);
        }
    } catch (err) {
        console.error(err);
    }
}

async function requestLoan() {
    const amountInput = document.getElementById('loan-amount-input');
    const amount = amountInput.value.trim();
    if (!amount) return;

    // Show loading state
    transitionToStep(3);
    const title = document.getElementById('result-title');
    const msg = document.getElementById('result-message');
    const icon = document.getElementById('result-icon');

    title.textContent = "AI Underwriting in Progress...";
    msg.textContent = "Analyzing bureau data and policy compliance...";
    icon.textContent = "⌛";

    try {
        const response = await fetch('/api/underwrite', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ customer_id: currentCustomerId, amount: amount })
        });
        const data = await response.json();

        renderResult(data);
    } catch (err) {
        console.error(err);
    }
}

function renderResult(data) {
    const title = document.getElementById('result-title');
    const msg = document.getElementById('result-message');
    const icon = document.getElementById('result-icon');
    const sanctionArea = document.getElementById('sanction-link-area');
    const downloadBtn = document.getElementById('sanction-download');

    if (data.status === "APPROVED_INSTANT") {
        icon.textContent = "✅";
        icon.className = "success";
        title.textContent = "CASH-CANNON Sanction Firing!";
        msg.textContent = `Target Locked! Congratulations ${data.name}! Your loan has been sanctioned @ ${data.offered_rate}.`;
        sanctionArea.classList.remove('hidden');
        // This is a dummy link for the simulation
        downloadBtn.href = "#";
        downloadBtn.onclick = () => alert("Downloading: " + data.letter_url);
    }
    else if (data.status === "CONDITIONALLY_APPROVED") {
        icon.textContent = "❓";
        icon.className = "warning";
        title.textContent = "Conditional Approval";
        msg.textContent = data.message;
        sanctionArea.classList.add('hidden');
    }
    else {
        icon.textContent = "❌";
        icon.className = "failure";
        title.textContent = "Application Rejected";
        msg.textContent = data.reason;
        sanctionArea.classList.add('hidden');
    }
}

function transitionToStep(stepNum) {
    // Hide all steps
    document.querySelectorAll('.flow-step').forEach(s => s.classList.add('hidden'));
    document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));

    // Show specific step
    if (stepNum === 1) {
        document.getElementById('verification-form').classList.remove('hidden');
        document.getElementById('step-1').classList.add('active');
    } else if (stepNum === 2) {
        document.getElementById('sales-form').classList.remove('hidden');
        document.getElementById('step-2').classList.add('active');
    } else if (stepNum === 3) {
        document.getElementById('result-display').classList.remove('hidden');
        document.getElementById('step-3').classList.add('active');
    }
}

function resetFlow() {
    currentCustomerId = "";
    document.getElementById('customer-id-input').value = "";
    document.getElementById('loan-amount-input').value = "";
    transitionToStep(1);
}
