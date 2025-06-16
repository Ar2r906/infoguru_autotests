import pytest
import time
from datetime import timedelta


@pytest.fixture(autouse=True)
def track_test_time(request):
    start_time = time.perf_counter()
    yield
    duration = timedelta(seconds=time.perf_counter() - start_time)

    # Добавляем время выполнения в отчет pytest
    request.node.user_properties.append(("duration", duration.total_seconds()))

    # Логируем в консоль
    if hasattr(request.config, "workerinput"):  # для pytest-xdist
        return
    print(f"\n[Test Duration] {request.node.name}: {duration.total_seconds():.3f}s")