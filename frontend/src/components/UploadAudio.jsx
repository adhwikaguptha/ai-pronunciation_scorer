import { useState } from "react";
import { analyzePronunciation } from "../services/api";

function UploadAudio({ setResult }) {
  const [audio, setAudio] = useState(null);
  const [referenceText, setReferenceText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!audio) {
      alert("Please upload an audio file.");
      return;
    }

    if (!referenceText.trim()) {
      alert("Please enter the reference text.");
      return;
    }

    const formData = new FormData();

    formData.append("audio", audio);
    formData.append("reference_text", referenceText);

    try {
      setLoading(true);

      const result = await analyzePronunciation(formData);

      setResult(result);
    } catch (error) {
      console.error(error);

      alert("Error analyzing pronunciation.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <form onSubmit={handleSubmit}>

        <label>Reference Text</label>

        <textarea
          rows="5"
          placeholder="Enter the sentence spoken in the audio..."
          value={referenceText}
          onChange={(e) => setReferenceText(e.target.value)}
        />

        <label>Upload Audio</label>

        <input
          type="file"
          accept="audio/*"
          onChange={(e) => setAudio(e.target.files[0])}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>

      </form>
    </div>
  );
}

export default UploadAudio;