package lk.ijse.gdse.orderservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author Prabodha Thathsarani
 * @date 2/19/25
 * @project supermarket-microservice
 **/

@RestController
@RequestMapping("/orders")
public class OrderController {
    @GetMapping("/all")
    public String getOrders(){
        return "orders: orders1, orders2, orders3";
    }
}



