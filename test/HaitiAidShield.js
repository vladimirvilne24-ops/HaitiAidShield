const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("HaitiAidShield", function () {
    let HaitiAidShield;
    let haitiAidShield;
    let owner, trustee2, trustee3, nonTrustee, recipient;

    beforeEach(async function () {
        [owner, trustee2, trustee3, nonTrustee, recipient] = await ethers.getSigners();

        HaitiAidShield = await ethers.getContractFactory("HaitiAidShield");

        haitiAidShield = await HaitiAidShield.deploy(
            [owner.address, trustee2.address, trustee3.address],
            2
        );

        await haitiAidShield.waitForDeployment();
    });

    it("Should deploy successfully", async function () {
        expect(await haitiAidShield.getAddress()).to.not.equal(
            "0x0000000000000000000000000000000000000000"
        );
    });

    it("Should initialize the required number of signatures", async function () {
        expect(await haitiAidShield.requiredSignatures()).to.equal(2);
    });

    it("Should allow a trustee to create an aid request", async function () {
        await haitiAidShield.proposeAid(
            "Medical Supplies",
            ethers.parseEther("1"),
            recipient.address
        );

        const request = await haitiAidShield.requests(1);

        expect(request.description).to.equal("Medical Supplies");
        expect(request.amount).to.equal(ethers.parseEther("1"));
    });

    it("Should reject aid requests from non-trustees", async function () {
        await expect(
            haitiAidShield
                .connect(nonTrustee)
                .proposeAid(
                    "Food",
                    ethers.parseEther("1"),
                    recipient.address
                )
        ).to.be.revertedWith("Access Denied: Not a registered Trustee");
    });

    it("Should prevent duplicate approvals", async function () {
        await haitiAidShield.proposeAid(
            "Food",
            ethers.parseEther("1"),
            recipient.address
        );

        await haitiAidShield.approveAid(1);

        await expect(
            haitiAidShield.approveAid(1)
        ).to.be.revertedWith("Trustee already approved this request");
    });

    it("Should automatically disburse funds after two approvals", async function () {
        await owner.sendTransaction({
            to: await haitiAidShield.getAddress(),
            value: ethers.parseEther("5"),
        });

        await haitiAidShield.proposeAid(
            "Emergency Relief",
            ethers.parseEther("1"),
            recipient.address
        );

        await haitiAidShield.approveAid(1);
        await haitiAidShield.connect(trustee2).approveAid(1);

        const request = await haitiAidShield.requests(1);

        expect(request.executed).to.equal(true);
    });

    it("Should return the correct contract balance", async function () {
        await owner.sendTransaction({
            to: await haitiAidShield.getAddress(),
            value: ethers.parseEther("5"),
        });

        const balance = await haitiAidShield.getContractBalance();

        expect(balance).to.equal(ethers.parseEther("5"));
    });
});