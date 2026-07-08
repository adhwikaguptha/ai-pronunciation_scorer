function Transcript({

    reference,

    transcript

}) {

    return (

        <div className="card">

            <h2>Transcript Comparison</h2>

            <div style={{ marginBottom: "20px" }}>

                <h3>Reference Text</h3>

                <p>{reference}</p>

            </div>

            <div>

                <h3>Recognized Speech</h3>

                <p>{transcript}</p>

            </div>

        </div>

    );

}

export default Transcript;