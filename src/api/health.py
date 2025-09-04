from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    return {
        """
            status": "I don't want the future.
            I want the present to stand still.
        """
    }
