from django.shortcuts import render, redirect
from django.views import View
from django.db import connection

class ManagePaymentsView(View):

    def Payments(request):
        
        ComandoSQL = "select date_delivery , C.first_name , C.last_name , printf('$%.2f', sum(quantity * price))  as Total"
        ComandoSQL += " from store_order O , store_customer C "
        ComandoSQL += " where status = 3 "
        ComandoSQL += " and O.customer_id = C.id "
        ComandoSQL += " group by date_delivery , O.customer_id "
        ComandoSQL += " order by date_delivery DESC "

        cursor_manage_order = connection.cursor()
        cursor_manage_order.execute(ComandoSQL)
        data_manage_order = cursor_manage_order.fetchall()
        context = {'manage_payments':data_manage_order}
        return render(request , 'manage_payments.html'  , context)

