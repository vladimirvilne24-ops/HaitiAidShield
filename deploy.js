const hre = require("hardhat");

async function main() {
  console.log("Starting deployment of HaitiAidShield...");

  // Get the account that is deploying the contract
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying with account:", deployer.address);

  // Get the Contract Factory
  const HaitiAid = await hre.ethers.getContractFactory("HaitiAidShield");

  /**
   * FIXING THE CONSTRUCTOR ERROR:
   * We are passing [deployer.address] as the array of trustees
   * and '1' as the number of required signatures.
   */
  const contract = await HaitiAid.deploy([deployer.address], 1);

  // Wait for the deployment to finish
  await contract.waitForDeployment();

  console.log("-----------------------------------------------");
  console.log("Success! HaitiAidShield deployed to:", contract.target);
  console.log("-----------------------------------------------");
}

main().catch((error) => {
  console.error("Deployment failed:", error);
  process.exitCode = 1;
});