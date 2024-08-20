package com.thanh.demojpa.controller;

import com.google.gson.Gson;
import com.thanh.demojpa.entity.Products;
import com.thanh.demojpa.entity.ShoppingCart;
import com.thanh.demojpa.entity.ShoppingCartItem;
import com.thanh.demojpa.repository.IProductsRepository;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class ShoppingController {
    private final String SHOPPING_CART_SESSION = "shoping_cart";
    @Autowired
    private IProductsRepository productRepository;
    @PostMapping("/shopping/addtocart")

    public String AddToCart(Long productId, HttpSession session)
    {
        Gson gson = new Gson();
        //Get shopping cart from session
        String cartInJson = (String) session.getAttribute(SHOPPING_CART_SESSION);
        ShoppingCart cart=null;
        //khoi tao neu chua co
        if(cartInJson==null)
            cart = new ShoppingCart();
        else
        {
            cart =gson.fromJson(cartInJson, ShoppingCart.class);
        }
        Products product = productRepository.findById(productId).get();
        ShoppingCartItem cartItem = new ShoppingCartItem();
        cartItem.product = product;
        cartItem.Qty =1;
        cart.items.add(cartItem);


        session.setAttribute(SHOPPING_CART_SESSION, gson.toJson(cart));
        return "redirect:/shopping/view";
    }

    @GetMapping("/shopping/view")
    public String ViewShopping(final Model model, HttpSession session)
    {
        Gson gson = new Gson();
        String cartInJson = (String) session.getAttribute(SHOPPING_CART_SESSION);
        ShoppingCart cart = gson.fromJson(cartInJson, ShoppingCart.class);

        model.addAttribute("cart", cart);
        return "shoppingcart";
    }
}
