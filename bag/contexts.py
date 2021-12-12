from django.shortcuts import get_object_or_404
from programs.models import Program

def bag_contents(request):

    bag_items = []
    total = 0 
    program_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        program = get_object_or_404(Program, pk=item_id)
        total += quantity * program.price
        program_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'program': program,
        })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'program_count': program_count,
    }

    return context