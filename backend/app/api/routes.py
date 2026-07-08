from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.pronunciation_service import PronunciationService

router = APIRouter(
    prefix="/api",
    tags=["Pronunciation Analyzer"]
)


@router.post("/analyze")
async def analyze_pronunciation(
    audio: UploadFile = File(...),
    reference_text: str = Form(...)
):
    """
    Analyze pronunciation.

    Parameters
    ----------
    audio
        Audio file uploaded by the user.

    reference_text
        The original sentence or paragraph.
    """

    if not reference_text.strip():

        raise HTTPException(
            status_code=400,
            detail="Reference text cannot be empty."
        )

    result = await PronunciationService.analyze(
        audio,
        reference_text
    )

    return result