from rest_framework.filters import BaseFilterBackend

from bank.constants import IFSC, BANK, CITY


class BankFilters(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = get_filters(request)
        if filters:
            return queryset.filter(**filters)
        else:
            return queryset


def get_filters(request):
    """Get the filters.

    Example:
        domain.com/bank/branches/?ifsc=ABHY0065001
        domain.com/bank/branches/?bank=ABHYUDAYA
        domain.com/bank/branches/?bank=ABHYUDAYA&city=mumbai
    """
    main_filter = {}
    try:
        for key in request.query_params:
            # splitting the last '/' in the url
            value = request.query_params[key].split('/')[0]

            if key == IFSC:
                main_filter['ifsc'] = value
            elif key == BANK:
                main_filter['bank__name__icontains'] = value
            elif key == CITY:
                main_filter['city__icontains'] = value
    except:
        # skip in exception
        pass

    return main_filter
