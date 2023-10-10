from django.shortcuts import render, redirect
from django.views import View
from django.db import connection

class ManageOrderView(View):

    def Orders(request, status=-1):
        
        ComandoSQL = f"select O.id , C.first_name , C.last_name , O.quantity , P.name , O.price , O.date_delivery, O.status , substr(O.address,1,50) "
        ComandoSQL += f" from store_order O , store_customer C , store_products P "
        ComandoSQL += f" where O.customer_id = C.id "
        ComandoSQL += f" and O.product_id = P.id "
        ComandoSQL += f" and O.status = {status}"
        ComandoSQL += f" order by O.date_delivery , C.first_name"

        cursor_manage_order = connection.cursor()
        cursor_manage_order.execute(ComandoSQL)
        data_manage_order = cursor_manage_order.fetchall()

        match status:
            case 0:
                tipo_consulta = "New Orders"
            case 1:
                tipo_consulta = "In Preparation"
            case 2:
                tipo_consulta = "Ready"
            case 3:
                tipo_consulta = "Delivered"
            case 9:
                tipo_consulta = "Cancelled"


        context = {'manage_orders':data_manage_order, 'tipo_consulta':tipo_consulta}
        return render(request , 'manage_orders.html'  , context)


    def Update_Orders(request, ID, status):

        ComandoSQL = f"select status from store_order where ID = {ID}"
        cursor_manage_order = connection.cursor()
        cursor_manage_order.execute(ComandoSQL)
        dados = cursor_manage_order.fetchone()
        status_atual = dados[0]
        cursor_manage_order.close
        
        cursor_manage_order2 = connection.cursor()
        ComandoSQL = f"update store_order set status = {status} where ID = {ID}"
        cursor_manage_order2.execute(ComandoSQL)
        cursor_manage_order2.close

        if int(status_atual) == 0:
            return redirect(f"/manage_orders/0")

        if int(status_atual) == 1:
            return redirect(f"/manage_orders/1")
        
        if int(status_atual) == 2:
            return redirect(f"/manage_orders/2")

        if int(status_atual) == 3:
            return redirect(f"/manage_orders/3")

        if int(status_atual) == 9:
            return redirect(f"/manage_orders/9")
