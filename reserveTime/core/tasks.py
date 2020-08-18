from celery.decorators import task
from restaurant.models import Table,TableDate,Time



@task(name="complete_reserve")
def complete_reserve(time, date, table_id):

    reserve_date = TableDate.objects.filter(date=date)
    table = Table.objects.filter(id = table_id, dates__in=reserve_date)
    reserve_time = table.times.filter(free_time=time).update(reserved=False)

    return reserve_time
