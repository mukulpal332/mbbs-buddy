import os

# Folder structure
folders = [
    "mbbs-buddy/public",
    "mbbs-buddy/src/components",
    "mbbs-buddy/src/utils"
]

# Files and content
files = {
    "mbbs-buddy/package.json": '''{
  "name": "mbbs-buddy",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "axios": "^1.4.0",
    "react-toastify": "^9.1.1",
    "workbox-window": "^7.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}''',

    "mbbs-buddy/public/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBBS Buddy</title>
</head>
<body style="background-color:black;color:white;">
  <div id="root"></div>
</body>
</html>''',

    "mbbs-buddy/src/index.js": '''import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
ReactDOM.render(<App />, document.getElementById("root"));''',

    "mbbs-buddy/src/App.jsx": '''import React from "react";
function App() {
  return (
    <div style={{ background: "#000", color: "#fff", height: "100vh", padding: "20px" }}>
      <h1>MBBS Buddy</h1>
      <p>Add Topic → Auto Schedule Revisions</p>
    </div>
  );
}
export default App;''',

    "mbbs-buddy/src/utils/spacedRepetition.js": '''export const generateRevisionSchedule = (startDate) => {
  const intervals = [1, 3, 7, 15, 30, 60, 90];
  return intervals.map(days => {
    const date = new Date(startDate);
    date.setDate(date.getDate() + days);
    return { day: `Day ${days}`, date: date.toISOString().split("T")[0] };
  });
};'''
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)

print("✅ MBBS Buddy folder created successfully!")

