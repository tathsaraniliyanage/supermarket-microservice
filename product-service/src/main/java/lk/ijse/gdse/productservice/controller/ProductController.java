package lk.ijse.gdse.productservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author Prabodha Thathsarani
 * @date 2/19/25
 * @project supermarket-microservice
 **/

@RestController
@RequestMapping("/product")
public class ProductController {

    @GetMapping("/all")
    public String getProduct(){
        return "product: prod1, prod2, prod3";
    }
}
