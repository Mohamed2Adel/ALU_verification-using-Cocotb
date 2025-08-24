import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.result import *


    ####start the test values###
#first test the reset
async def areset_test(dut):
    dut.areset.value = 0
    dut.A.value = 5
    dut.B.value = 3
    dut.opcode.value = 2
    ##no need for delay since it is asynchronous reset
    expected_C = 0
    expected_arith_flag = 0
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0
    await Timer(1, units="ns")  # Wait for the reset to take effect
    if dut.C.value != expected_C:
        raise TestFailure('result of reset is not correct ')
    else:
        cocotb.log.info('reset test passed')
    #assert dut.C.value == expected_C, f"reset failed: {dut.C.value} != {expected_C}"
    assert dut.arith_flag.value == expected_arith_flag, f"reset failed: {dut.arith_flag.value} != {expected_arith_flag}"
    assert dut.logic_flag.value == expected_logic_flag, f"reset failed: {dut.logic_flag.value} != {expected_logic_flag}"
    assert dut.N_flag.value == expected_N_flag, f"reset failed: {dut.N_flag.value} != {expected_N_flag}"
    assert dut.carry_flag.value == expected_carry_flag, f"reset failed: {dut.carry_flag.value} != {expected_carry_flag}"
    await Timer(10, units="ns")  # Wait for a short time to ensure stability
    dut.areset.value = 1  # Deactivate reset
    

#second check the addition
async def addition_test(dut):
    dut.A.value = 4
    dut.B.value = 6
    dut.opcode.value = 0
    ##no need for delay since it is asynchronous reset
    expected_C = 10
    expected_arith_flag = 1
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0
    await RisingEdge(dut.clk)  # Wait for a clock edge
    cocotb.log.info("after rising edge")
    await Timer(1, units="ns")  # Wait for the reset to take effect
    assert dut.C.value == expected_C, f"addition failed: {dut.C.value} != {expected_C}"
    assert dut.arith_flag.value == expected_arith_flag, f"addition failed: {dut.arith_flag.value} != {expected_arith_flag}"
    assert dut.logic_flag.value == expected_logic_flag, f"addition failed: {dut.logic_flag.value} != {expected_logic_flag}"
    assert dut.N_flag.value == expected_N_flag, f"addition failed: {dut.N_flag.value} != {expected_N_flag}"
    assert dut.carry_flag.value == expected_carry_flag, f"addition failed: {dut.carry_flag.value} != {expected_carry_flag}"
    await FallingEdge(dut.clk) 
    cocotb.log.info("after falling edge")


#third check the subtraction
async def subtraction_test(dut):
    dut.A.value = 10
    dut.B.value = 4
    dut.opcode.value = 1
    ##no need for delay since it is asynchronous reset
    expected_C = 6
    expected_arith_flag = 1
    expected_logic_flag = 0
    expected_N_flag = 0
    expected_carry_flag = 0
    await RisingEdge(dut.clk)  # Wait for a clock edge
    cocotb.log.info("after rising edge")
    await Timer(1, units="ns")  # Wait for the reset to take effect
    assert dut.C.value == expected_C, f"subtraction failed: {dut.C.value} != {expected_C}"
    assert dut.arith_flag.value == expected_arith_flag, f"subtraction failed: {dut.arith_flag.value} != {expected_arith_flag}"
    assert dut.logic_flag.value == expected_logic_flag, f"subtraction failed: {dut.logic_flag.value} != {expected_logic_flag}"
    assert dut.N_flag.value == expected_N_flag, f"subtraction failed: {dut.N_flag.value} != {expected_N_flag}"
    assert dut.carry_flag.value == expected_carry_flag, f"subtraction failed: {dut.carry_flag.value} != {expected_carry_flag}"
    await FallingEdge(dut.clk) 
    cocotb.log.info("after falling edge")

#fourth check the AND operation
async def and_test(dut):
    dut.A.value = 6  # 0110 in binary
    dut.B.value = 3  # 0011 in binary
    dut.opcode.value = 3
    ##no need for delay since it is asynchronous reset
    expected_C = 2  # 0010 in binary
    expected_arith_flag = 0
    expected_logic_flag = 1
    expected_N_flag = 0
    expected_carry_flag = 0
    await RisingEdge(dut.clk)  # Wait for a clock edge
    cocotb.log.info("after rising edge")
    await Timer(1, units="ns")  # Wait for the reset to take effect
    assert dut.C.value == expected_C, f"ANDING failed: {dut.C.value} != {expected_C}"
    assert dut.arith_flag.value == expected_arith_flag, f"ANDING failed: {dut.arith_flag.value} != {expected_arith_flag}"
    assert dut.logic_flag.value == expected_logic_flag, f"ANDING failed: {dut.logic_flag.value} != {expected_logic_flag}"
    assert dut.N_flag.value == expected_N_flag, f"ANDING failed: {dut.N_flag.value} != {expected_N_flag}"
    assert dut.carry_flag.value == expected_carry_flag, f"ANDING failed: {dut.carry_flag.value} != {expected_carry_flag}"
    await FallingEdge(dut.clk) 
    cocotb.log.info("after falling edge")

#fifth check the OR operation
async def or_test(dut):
    dut.A.value = 6  # 0110 in binary
    dut.B.value = 3  # 0011 in binary
    dut.opcode.value = 4
    ##no need for delay since it is asynchronous reset
    expected_C = 7  # 0111 in binary
    expected_arith_flag = 0
    expected_logic_flag = 1
    expected_N_flag = 0
    expected_carry_flag = 0
    await RisingEdge(dut.clk)  # Wait for a clock edge
    cocotb.log.info("after rising edge")
    await Timer(1, units="ns")  # Wait for the reset to take effect
    assert dut.C.value == expected_C, f"ORING failed: {dut.C.value} != {expected_C}"
    assert dut.arith_flag.value == expected_arith_flag, f"ORING failed: {dut.arith_flag.value} != {expected_arith_flag}"
    assert dut.logic_flag.value == expected_logic_flag, f"ORING failed: {dut.logic_flag.value} != {expected_logic_flag}"
    assert dut.N_flag.value == expected_N_flag, f"ORING failed: {dut.N_flag.value} != {expected_N_flag}"
    assert dut.carry_flag.value == expected_carry_flag, f"ORING failed: {dut.carry_flag.value} != {expected_carry_flag}"
    await FallingEdge(dut.clk) 
    cocotb.log.info("after falling edge")


@cocotb.test()
async def ALU_top(dut):
    cocotb.log.info("Starting ALU test...")
    
    # clock generation
    clock = Clock(dut.clk, 10, units="ns")  # 10 ns clock period
    cocotb.start_soon(clock.start())

    # Run the tests in sequence
    await cocotb.start_soon(areset_test(dut))
    await cocotb.start_soon(addition_test(dut))
    await cocotb.start_soon(subtraction_test(dut))
    await cocotb.start_soon(and_test(dut))
    await cocotb.start_soon(or_test(dut))