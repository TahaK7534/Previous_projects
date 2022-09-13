using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playermovement : MonoBehaviour
{

    public CharacterController2D Charecter;
    public Animator animator;
    public float runSpeed = 40f;

    float horixontalMove = 0f;

    bool Jump = false;
    bool crouch = false;
    

    
    

    // Update is called once per frame
    void Update()
    {
       horixontalMove = Input.GetAxisRaw("Horizontal") * runSpeed;
       animator.SetFloat("Speed", Mathf.Abs(horixontalMove));
       if (Input.GetButtonDown("Jump"))
       {
        Jump = true;
       }

       if (Input.GetButtonDown("Crouch"))

       {
        crouch = true;

       } else if (Input.GetButtonUp("Crouch"))
       {
         crouch = false;
       }

    }


    void FixedUpdate()
    {
        
      Charecter.Move(horixontalMove * Time.fixedDeltaTime, crouch, Jump);
      Jump = false;
      
    }

}
