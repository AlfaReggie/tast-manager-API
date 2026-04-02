from pydantic import BaseModel


class TasksSummaryRead(BaseModel):
    total_tasks: int
    new_tasks: int
    in_progress_tasks: int
    done_tasks: int
    completion_rate: float