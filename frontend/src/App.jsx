import { useState } from "react";

import UploadAudio from "./components/UploadAudio";
import ScoreCard from "./components/ScoreCard";
import Transcript from "./components/Transcript";
import AnalysisTable from "./components/AnalysisTable";
import FeedbackList from "./components/FeedbackList";

import "./index.css";

function App() {

  const [result, setResult] = useState(null);

  return (

    <div className="container">

      <h1>AI Pronunciation Analyzer</h1>

      <p className="subtitle">
        Upload an English audio clip and compare it with the reference text using AI-powered pronunciation analysis.
      </p>

      <div className="card">

        <h2>📌 Audio Requirements</h2>

        <ul>
          <li><strong>Duration:</strong> 30–45 seconds</li>
          <li><strong>Language:</strong> English</li>
          <li><strong>Supported Formats:</strong> WAV, MP3, M4A, OGG, OGA, OPUS, FLAC, WEBM</li>
          <li><strong>Reference Text:</strong> The spoken audio should match the text entered in the Reference Text field.</li>
          <li><strong>Recording Quality:</strong> Record in a quiet environment and speak clearly for the best pronunciation analysis.</li>
          <li><strong>Privacy:</strong> Uploaded audio is processed only for analysis and is automatically deleted after processing.</li>
        </ul>

      </div>

      <UploadAudio setResult={setResult} />

      {result && (

        <>

          <ScoreCard
            score={result.score}
            accuracy={result.accuracy}
            language={result.language}
            languageProbability={result.language_probability}
          />

          <Transcript
            reference={result.reference_text}
            transcript={result.transcript}
          />

          <AnalysisTable
            analysis={result.analysis}
          />

          <FeedbackList
            feedback={result.feedback}
          />

        </>

      )}

    </div>

  );

}

export default App;