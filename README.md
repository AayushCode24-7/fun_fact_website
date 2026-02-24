# 🚫 The Scriptless Sandbox

A collection of interactive web experiments built with a strict **"No JavaScript"** policy. This repository explores the power of the DOM and CSS selectors to handle state, logic, and interactivity.

---

## 🛠 The Philosophy
Why use 10 lines of JavaScript when you can use 50 lines of complex CSS? This project is a technical challenge to push the boundaries of what is possible using only:
* **HTML5** for structure and state storage.
* **CSS3** for logic, layout, and animations.

## 🕹 Features & Techniques
This repo demonstrates several "No-JS" workarounds for common UI tasks:

### 1. State Management (The Checkbox Hack)
We use hidden `<input type="checkbox">` and `<input type="radio">` elements to act as variables. By monitoring the `:checked` pseudo-class, we can toggle the visibility and style of other elements on the page.



### 2. Sequential Interaction
Using **stacked labels**, we create buttons that appear to "remember" clicks. Each click reveals a new label for the next hidden input, allowing for step-by-step content reveals or multi-stage processes.

### 3. Logic Gates with CSS
By utilizing the **General Sibling Selector (`~`)**, we create "If-Then" logic gates:
* *If* Input A is checked...
* *Then* change the property of Box B.



### 4. Zero-Script Animations
All motion is handled via `@keyframes` and CSS transitions, ensuring a lightweight and performant experience that works even if the user has disabled scripts entirely.

---

## 📂 Project Structure
* **`index.html`**: The core file containing the layout, "logic" inputs, and styling.
* **Style Layer**: Integrated CSS using modern variables for easy theme swapping.
* **Logic Layer**: Purely HTML-based state triggers.

## 🚀 How to Explore
1.  Clone the repository: `git clone https://github.com/yourusername/your-repo-name.git`
2.  Open `index.html` in any modern browser.
3.  Interact with the UI and notice the lack of network requests or script executions.

---

## 🚧 Roadmap
- [x] Multi-stage "Next" button logic.
- [x] Category-based content filtering.
- [ ] CSS-only tooltips and modals.
- [ ] Full-page layout transitions without navigation.

**Made with 100% Logic and 0% Scripts.**
