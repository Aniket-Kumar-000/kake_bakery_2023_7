def config_pvlan(dut,primary_vlan,Iso,com,Isolated,community1,community2):
    cmd = f"""vlan {primary_vlan}
             private-vlan primary
             private-vlan association add {Iso}-{com}
             no shutdown
             exit
             vlan {Isolated}
             private-vlan Isolated
             no shutdown    
             exit
             vlan {community1}-{community2}
             private-vlan community
             no shutdown
             exit
          """
    status = True
    try:
        log.info("pvlan configuration made successfully") 
        dut.configure(cmd)
        
    except Exception as e:
        log.error("Error in CLI configuration on {} \nExiting error: {}".format(dut.name, e))
        status = False
    return status
